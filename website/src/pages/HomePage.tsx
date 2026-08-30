import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, BookOpen, Code, Lightbulb, LinkSimple, Star, CheckCircle } from '@phosphor-icons/react';
import { RibbonFieldBackground } from '../components/animations/RibbonFieldBackground';
import { getTopicTree, getStats } from '../services/contentService';

interface HomePageProps {
  heroHue?: number;
  onOpenDonate: () => void;
}

export const HomePage: React.FC<HomePageProps> = ({ heroHue = 0 }) => {
  const topics = getTopicTree();
  const stats = getStats();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', width: '100%' }}>
      {/* 1. HERO SECTION with RibbonField WebGL (16:9 Aspect Ratio) */}
      <section
        style={{
          position: 'relative',
          width: '100%',
          aspectRatio: '16 / 9',
          minHeight: 'clamp(480px, 56.25vw, 680px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '48px 24px',
          borderBottom: '1px solid var(--color-hairline)',
          overflow: 'hidden',
          backgroundColor: 'var(--color-canvas)'
        }}
      >
        <RibbonFieldBackground hue={heroHue} speed={1.0} />

        <div
          style={{
            position: 'relative',
            zIndex: 10,
            maxWidth: '800px',
            margin: '0 auto',
            textAlign: 'center',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: '20px'
          }}
        >
          {/* Badge */}
          <div
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '4px 12px',
              backgroundColor: 'rgba(255, 255, 255, 0.06)',
              border: '1px solid var(--color-hairline-strong)',
              borderRadius: 'var(--radius-full)',
              fontSize: '12px',
              fontWeight: 500,
              color: 'var(--color-ink)',
              backdropFilter: 'blur(8px)'
            }}
          >
            <CheckCircle size={14} color="#4ade80" />
            <span>Structured Python 3.12+ Knowledge Base</span>
          </div>

          {/* Title */}
          <h1
            style={{
              fontFamily: 'var(--font-serif)',
              fontStyle: 'italic',
              fontWeight: 700,
              fontSize: 'clamp(2.5rem, 5vw, 3.75rem)',
              color: 'var(--color-on-dark)',
              lineHeight: 1.1,
              letterSpacing: '-0.02em',
              textShadow: '0 2px 10px rgba(0, 0, 0, 0.8)'
            }}
          >
            python-learning
          </h1>

          {/* Subtitle */}
          <p
            style={{
              fontSize: 'clamp(1rem, 2vw, 1.15rem)',
              color: 'var(--color-body)',
              lineHeight: 1.6,
              maxWidth: '620px',
              textShadow: '0 1px 4px rgba(0, 0, 0, 0.9)'
            }}
          >
            A high-performance, in-depth technical knowledge repository covering Python from low-level CPython execution, bytecode, and memory models to advanced language paradigms.
          </p>

          {/* CTAs */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '14px', marginTop: '12px', flexWrap: 'wrap', justifyContent: 'center' }}>
            <Link to="/notes" className="btn-primary" style={{ height: '42px', padding: '0 22px', fontSize: '15px' }}>
              <span>Explore Notes</span>
              <ArrowRight size={16} />
            </Link>
            <a
              href="https://github.com/notdgx/python-learning"
              target="_blank"
              rel="noopener noreferrer"
              className="btn-secondary"
              style={{ height: '42px', padding: '0 20px', fontSize: '15px' }}
            >
              <span>View on GitHub</span>
              <Star size={16} />
            </a>
          </div>

          {/* Quick Metrics */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '32px',
              marginTop: '24px',
              paddingTop: '20px',
              borderTop: '1px solid var(--color-hairline-soft)',
              color: 'var(--color-mute)',
              fontSize: '13px'
            }}
          >
            <div>
              <strong style={{ color: 'var(--color-ink)', fontSize: '16px' }}>{stats.notes}</strong> Active Notes
            </div>
            <div>
              <strong style={{ color: 'var(--color-ink)', fontSize: '16px' }}>{stats.subtopics}</strong> Subtopics
            </div>
          </div>
        </div>
      </section>

      {/* 2. LEARNING MODULES / TOPICS */}
      <section style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto', padding: '72px 24px', width: '100%' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '32px', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--color-mute)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
              Curriculum Overview
            </span>
            <h2 style={{ fontSize: '1.85rem', color: 'var(--color-ink)', marginTop: '4px' }}>
              Structured Learning Topics
            </h2>
          </div>
          <Link to="/notes" style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontSize: '14px', color: 'var(--color-ink)' }}>
            <span>Browse complete roadmap</span>
            <ArrowRight size={14} />
          </Link>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '20px' }}>
          {topics.map((topic) => (
            <div
              key={topic.id}
              className="surface-card"
              style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '20px' }}
            >
              <div>
                <div
                  style={{
                    width: '36px',
                    height: '36px',
                    borderRadius: 'var(--radius-md)',
                    backgroundColor: 'var(--color-surface-card)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: 'var(--color-ink)',
                    marginBottom: '14px'
                  }}
                >
                  <BookOpen size={20} />
                </div>
                <h3 style={{ fontSize: '1.2rem', color: 'var(--color-ink)', marginBottom: '8px' }}>
                  {topic.title}
                </h3>
                <p style={{ fontSize: '13.5px', color: 'var(--color-mute)', lineHeight: 1.6, marginBottom: '16px' }}>
                  Foundational Python concepts, internal execution mechanisms, object models, and execution architecture.
                </p>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {topic.subtopics.map((st) => (
                    <div key={st.id} style={{ fontSize: '13px', color: 'var(--color-charcoal)', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <span style={{ color: 'var(--color-stone)' }}>•</span>
                      <span>{st.title} ({st.notes.length} notes)</span>
                    </div>
                  ))}
                </div>
              </div>

              <Link
                to={topic.subtopics[0]?.notes[0]?.route || '/notes'}
                className="btn-secondary"
                style={{ width: '100%', justifyContent: 'space-between' }}
              >
                <span>Start Topic</span>
                <ArrowRight size={14} />
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* 3. PROJECTS & PRACTICE PREVIEW */}
      <section style={{ backgroundColor: 'var(--color-surface)', borderTop: '1px solid var(--color-hairline)', borderBottom: '1px solid var(--color-hairline)', padding: '72px 24px' }}>
        <div style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto' }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '32px' }}>
            {/* Projects Box */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div style={{ width: '36px', height: '36px', borderRadius: 'var(--radius-md)', backgroundColor: 'var(--color-surface-elevated)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--color-ink)' }}>
                <Code size={20} />
              </div>
              <h3 style={{ fontSize: '1.3rem', color: 'var(--color-ink)' }}>Hands-on Projects</h3>
              <p style={{ fontSize: '14px', color: 'var(--color-mute)', lineHeight: 1.6 }}>
                Real-world scripts, CLI utilities, and architectural implementations designed to apply core Python theory in production environments.
              </p>
              <Link to="/projects" className="btn-secondary" style={{ width: 'fit-content', marginTop: '8px' }}>
                <span>View Projects</span>
                <ArrowRight size={14} />
              </Link>
            </div>

            {/* Practice Box */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div style={{ width: '36px', height: '36px', borderRadius: 'var(--radius-md)', backgroundColor: 'var(--color-surface-elevated)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--color-ink)' }}>
                <Lightbulb size={20} />
              </div>
              <h3 style={{ fontSize: '1.3rem', color: 'var(--color-ink)' }}>Interview & Practice Questions</h3>
              <p style={{ fontSize: '14px', color: 'var(--color-mute)', lineHeight: 1.6 }}>
                Curated technical questions, intermediate-to-advanced challenges, and annotated solution walkthroughs.
              </p>
              <Link to="/practice" className="btn-secondary" style={{ width: 'fit-content', marginTop: '8px' }}>
                <span>Explore Practice</span>
                <ArrowRight size={14} />
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* 4. CURATED RESOURCES PREVIEW */}
      <section style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto', padding: '72px 24px', width: '100%' }}>
        <div style={{ textAlign: 'center', maxWidth: '600px', margin: '0 auto 40px' }}>
          <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--color-mute)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
            Ecosystem
          </span>
          <h2 style={{ fontSize: '1.85rem', color: 'var(--color-ink)', marginTop: '4px', marginBottom: '8px' }}>
            External Resources & Links
          </h2>
          <p style={{ fontSize: '14px', color: 'var(--color-mute)' }}>
            Curated channels, official documentation, social accounts, and repository tools.
          </p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '16px' }}>
          <a
            href="https://docs.python.org/3/"
            target="_blank"
            rel="noopener noreferrer"
            className="surface-card"
            style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '16px 20px' }}
          >
            <div>
              <h4 style={{ fontSize: '14px', color: 'var(--color-ink)' }}>Official Python Docs</h4>
              <span style={{ fontSize: '12px', color: 'var(--color-mute)' }}>python.org/3</span>
            </div>
            <LinkSimple size={18} color="var(--color-mute)" />
          </a>

          <a
            href="https://github.com/notdgx/"
            target="_blank"
            rel="noopener noreferrer"
            className="surface-card"
            style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '16px 20px' }}
          >
            <div>
              <h4 style={{ fontSize: '14px', color: 'var(--color-ink)' }}>notdgx GitHub</h4>
              <span style={{ fontSize: '12px', color: 'var(--color-mute)' }}>github.com/notdgx</span>
            </div>
            <LinkSimple size={18} color="var(--color-mute)" />
          </a>

          <a
            href="https://www.youtube.com/@notdgx"
            target="_blank"
            rel="noopener noreferrer"
            className="surface-card"
            style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '16px 20px' }}
          >
            <div>
              <h4 style={{ fontSize: '14px', color: 'var(--color-ink)' }}>notdgx YouTube</h4>
              <span style={{ fontSize: '12px', color: 'var(--color-mute)' }}>youtube.com/@notdgx</span>
            </div>
            <LinkSimple size={18} color="var(--color-mute)" />
          </a>
        </div>
      </section>
    </div>
  );
};
