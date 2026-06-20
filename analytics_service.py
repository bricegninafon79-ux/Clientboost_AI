"""
analytics_service.py - Analytics et Reporting pour ClientBoost AI
Suivre les performances, les tendances et les métriques d'utilisation
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from collections import Counter
import sqlite3

# ─────────────────────────────────────────────
# 1. DATABASE SETUP
# ─────────────────────────────────────────────

def init_analytics_db():
    """Initialiser la base de données SQLite pour les analytics"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    # Table des générations
    c.execute('''
        CREATE TABLE IF NOT EXISTS generations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            problem_id TEXT,
            problem_title TEXT,
            tone TEXT,
            language TEXT,
            sector TEXT,
            target_audience TEXT,
            pain_point TEXT,
            copy_length INTEGER,
            message_preview TEXT
        )
    ''')
    
    # Table des engagements utilisateur
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_engagement (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            action TEXT,
            action_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            details TEXT
        )
    ''')
    
    # Table des performances (reply rates, conversions)
    c.execute('''
        CREATE TABLE IF NOT EXISTS performance_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            generation_id INTEGER,
            sent_date DATETIME,
            reply_date DATETIME,
            replied BOOLEAN,
            conversion BOOLEAN,
            conversion_value REAL,
            feedback_text TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# ─────────────────────────────────────────────
# 2. DATA COLLECTION FUNCTIONS
# ─────────────────────────────────────────────

def log_generation(user_id, problem_id, problem_title, tone, language, sector, target, pain_point, message):
    """Enregistrer une génération de message"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO generations 
        (user_id, problem_id, problem_title, tone, language, sector, target_audience, pain_point, copy_length, message_preview)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, problem_id, problem_title, tone, language, sector, target, pain_point, len(message), message[:100]))
    
    conn.commit()
    conn.close()

def log_user_action(user_id, action, details=""):
    """Enregistrer une action utilisateur (click, save, share, etc)"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO user_engagement (user_id, action, details)
        VALUES (?, ?, ?)
    ''', (user_id, action, details))
    
    conn.commit()
    conn.close()

def log_performance(user_id, generation_id, sent_date, replied, conversion=False, conversion_value=0):
    """Enregistrer les métriques de performance (réponses, conversions)"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    reply_date = datetime.now() if replied else None
    
    c.execute('''
        INSERT INTO performance_metrics 
        (user_id, generation_id, sent_date, reply_date, replied, conversion, conversion_value)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, generation_id, sent_date, reply_date, replied, conversion, conversion_value))
    
    conn.commit()
    conn.close()

# ─────────────────────────────────────────────
# 3. ANALYTICS QUERY FUNCTIONS
# ─────────────────────────────────────────────

def get_user_stats(user_id):
    """Obtenir les stats globales d'un utilisateur"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    # Total générations
    c.execute('SELECT COUNT(*) FROM generations WHERE user_id = ?', (user_id,))
    total_gen = c.fetchone()[0]
    
    # Dernière génération
    c.execute('''
        SELECT MAX(timestamp) FROM generations WHERE user_id = ?
    ''', (user_id,))
    last_gen = c.fetchone()[0]
    
    # Génération aujourd'hui
    today = datetime.now().date()
    c.execute('''
        SELECT COUNT(*) FROM generations 
        WHERE user_id = ? AND DATE(timestamp) = ?
    ''', (user_id, today))
    today_gen = c.fetchone()[0]
    
    # Reply rate (si données disponibles)
    c.execute('''
        SELECT COUNT(*) FROM performance_metrics WHERE user_id = ? AND replied = 1
    ''', (user_id,))
    replies = c.fetchone()[0]
    
    c.execute('''
        SELECT COUNT(*) FROM performance_metrics WHERE user_id = ?
    ''', (user_id,))
    total_tracked = c.fetchone()[0]
    
    reply_rate = (replies / total_tracked * 100) if total_tracked > 0 else 0
    
    conn.close()
    
    return {
        "total_generations": total_gen,
        "last_generation": last_gen,
        "today_generations": today_gen,
        "reply_rate": reply_rate
    }

def get_problem_distribution(user_id):
    """Quelle problématique est la plus utilisée?"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT problem_title, COUNT(*) as count
        FROM generations
        WHERE user_id = ?
        GROUP BY problem_title
        ORDER BY count DESC
    ''', (user_id,))
    
    results = c.fetchall()
    conn.close()
    
    df = pd.DataFrame(results, columns=['Problem', 'Count'])
    return df

def get_tone_distribution(user_id):
    """Quel ton est le plus utilisé?"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT tone, COUNT(*) as count
        FROM generations
        WHERE user_id = ?
        GROUP BY tone
        ORDER BY count DESC
    ''', (user_id,))
    
    results = c.fetchall()
    conn.close()
    
    df = pd.DataFrame(results, columns=['Tone', 'Count'])
    return df

def get_language_distribution(user_id):
    """Quelle langue est la plus utilisée?"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT language, COUNT(*) as count
        FROM generations
        WHERE user_id = ?
        GROUP BY language
        ORDER BY count DESC
    ''', (user_id,))
    
    results = c.fetchall()
    conn.close()
    
    df = pd.DataFrame(results, columns=['Language', 'Count'])
    return df

def get_generation_trends(user_id, days=30):
    """Tendance des générations sur les 30 derniers jours"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT DATE(timestamp) as date, COUNT(*) as count
        FROM generations
        WHERE user_id = ? AND timestamp >= datetime('now', '-' || ? || ' days')
        GROUP BY DATE(timestamp)
        ORDER BY date
    ''', (user_id, days))
    
    results = c.fetchall()
    conn.close()
    
    df = pd.DataFrame(results, columns=['Date', 'Count'])
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_top_sectors(user_id):
    """Top 5 secteurs utilisés"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT sector, COUNT(*) as count
        FROM generations
        WHERE user_id = ? AND sector != ''
        GROUP BY sector
        ORDER BY count DESC
        LIMIT 5
    ''', (user_id,))
    
    results = c.fetchall()
    conn.close()
    
    df = pd.DataFrame(results, columns=['Sector', 'Count'])
    return df

def get_conversion_metrics(user_id):
    """Taux de conversion et ROI"""
    conn = sqlite3.connect('clientboost_analytics.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT 
            COUNT(*) as total,
            SUM(CASE WHEN replied = 1 THEN 1 ELSE 0 END) as replies,
            SUM(CASE WHEN conversion = 1 THEN 1 ELSE 0 END) as conversions,
            SUM(conversion_value) as revenue
        FROM performance_metrics
        WHERE user_id = ?
    ''', (user_id,))
    
    result = c.fetchone()
    conn.close()
    
    total, replies, conversions, revenue = result
    
    reply_rate = (replies / total * 100) if total and total > 0 else 0
    conversion_rate = (conversions / total * 100) if total and total > 0 else 0
    
    return {
        "total_tracked": total or 0,
        "replies": replies or 0,
        "conversions": conversions or 0,
        "revenue": revenue or 0,
        "reply_rate": reply_rate,
        "conversion_rate": conversion_rate
    }

# ─────────────────────────────────────────────
# 4. STREAMLIT DASHBOARD COMPONENTS
# ─────────────────────────────────────────────

def display_analytics_dashboard(user_id, language="en"):
    """Afficher le dashboard analytics complet dans Streamlit"""
    
    # Textes
    texts = {
        "en": {
            "title": "📊 Analytics Dashboard",
            "overview": "Overview",
            "trends": "Generation Trends",
            "distributions": "Usage Distributions",
            "performance": "Performance Metrics",
            "total_gen": "Total Generations",
            "today_gen": "Generated Today",
            "last_gen": "Last Generation",
            "reply_rate": "Reply Rate",
            "conversion_rate": "Conversion Rate",
            "revenue": "Revenue Generated",
            "problem_dist": "Problems Used",
            "tone_dist": "Tones Preferred",
            "language_dist": "Languages Used",
            "top_sectors": "Top Sectors",
        },
        "fr": {
            "title": "📊 Dashboard Analytique",
            "overview": "Aperçu",
            "trends": "Tendance des Générations",
            "distributions": "Distribution d'Utilisation",
            "performance": "Métriques de Performance",
            "total_gen": "Générations Totales",
            "today_gen": "Généré Aujourd'hui",
            "last_gen": "Dernière Génération",
            "reply_rate": "Taux de Réponse",
            "conversion_rate": "Taux de Conversion",
            "revenue": "Revenus Générés",
            "problem_dist": "Problèmes Utilisés",
            "tone_dist": "Tons Préférés",
            "language_dist": "Langues Utilisées",
            "top_sectors": "Top Secteurs",
        }
    }
    
    t = texts.get(language, texts["en"])
    
    # Initialiser la DB
    init_analytics_db()
    
    # Récupérer les données
    stats = get_user_stats(user_id)
    
    st.markdown(f"## {t['title']}")
    st.write("")
    
    # ── OVERVIEW ──
    st.markdown(f"### {t['overview']}")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(t['total_gen'], stats['total_generations'])
    with col2:
        st.metric(t['today_gen'], stats['today_generations'])
    with col3:
        last_gen_display = stats['last_generation'][:10] if stats['last_generation'] else "N/A"
        st.metric(t['last_gen'], last_gen_display)
    with col4:
        st.metric(t['reply_rate'], f"{stats['reply_rate']:.1f}%")
    
    st.write("")
    
    # ── TRENDS ──
    st.markdown(f"### {t['trends']}")
    trends_df = get_generation_trends(user_id, 30)
    
    if len(trends_df) > 0:
        fig_trends = px.line(
            trends_df, x='Date', y='Count',
            title='Messages générés par jour (30 derniers jours)',
            markers=True,
            template='plotly_white'
        )
        fig_trends.update_traces(line=dict(color='#0ea5e9', width=3))
        st.plotly_chart(fig_trends, use_container_width=True)
    else:
        st.info("Pas assez de données pour afficher les tendances")
    
    st.write("")
    
    # ── DISTRIBUTIONS ──
    st.markdown(f"### {t['distributions']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        problem_df = get_problem_distribution(user_id)
        if len(problem_df) > 0:
            fig_problem = px.pie(
                problem_df, values='Count', names='Problem',
                title=t['problem_dist'],
                template='plotly_white'
            )
            st.plotly_chart(fig_problem, use_container_width=True)
        else:
            st.info("Pas de données")
    
    with col2:
        tone_df = get_tone_distribution(user_id)
        if len(tone_df) > 0:
            fig_tone = px.bar(
                tone_df, x='Tone', y='Count',
                title=t['tone_dist'],
                template='plotly_white'
            )
            fig_tone.update_traces(marker=dict(color='#2563eb'))
            st.plotly_chart(fig_tone, use_container_width=True)
        else:
            st.info("Pas de données")
    
    st.write("")
    
    # ── TOP SECTORS ──
    st.markdown("### Top Sectors")
    sector_df = get_top_sectors(user_id)
    if len(sector_df) > 0:
        fig_sectors = px.bar(
            sector_df, x='Count', y='Sector',
            orientation='h',
            title=t['top_sectors'],
            template='plotly_white'
        )
        fig_sectors.update_traces(marker=dict(color='#10b981'))
        st.plotly_chart(fig_sectors, use_container_width=True)
    
    st.write("")
    
    # ── PERFORMANCE ──
    st.markdown(f"### {t['performance']}")
    perf = get_conversion_metrics(user_id)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Messages Suivis", perf['total_tracked'])
    with col2:
        st.metric("Réponses", perf['replies'])
    with col3:
        st.metric(t['conversion_rate'], f"{perf['conversion_rate']:.1f}%")
    with col4:
        st.metric(t['revenue'], f"${perf['revenue']:.2f}")

# ─────────────────────────────────────────────
# 5. EXPORT FUNCTIONS
# ─────────────────────────────────────────────

def export_analytics_csv(user_id):
    """Exporter les données analytiques en CSV"""
    conn = sqlite3.connect('clientboost_analytics.db')
    
    query = '''
        SELECT timestamp, problem_title, tone, language, sector, copy_length
        FROM generations
        WHERE user_id = ?
        ORDER BY timestamp DESC
    '''
    
    df = pd.read_sql_query(query, conn, params=(user_id,))
    conn.close()
    
    csv = df.to_csv(index=False)
    return csv

def export_analytics_pdf(user_id):
    """Exporter un rapport PDF (avec reportlab)"""
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    from io import BytesIO
    
    stats = get_user_stats(user_id)
    perf = get_conversion_metrics(user_id)
    
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph(f"<b>ClientBoost AI - Analytics Report</b>", styles['Heading1'])
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Stats table
    stats_data = [
        ['Metric', 'Value'],
        ['Total Generations', str(stats['total_generations'])],
        ['Today Generations', str(stats['today_generations'])],
        ['Reply Rate', f"{stats['reply_rate']:.1f}%"],
        ['Conversions', str(perf['conversions'])],
        ['Revenue', f"${perf['revenue']:.2f}"]
    ]
    
    stats_table = Table(stats_data)
    stats_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#0ea5e9'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), '#f0f9ff'),
        ('GRID', (0, 0), (-1, -1), 1, '#cccccc'),
    ]))
    
    elements.append(stats_table)
    
    doc.build(elements)
    buffer.seek(0)
    return buffer.getvalue()
