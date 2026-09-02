import React from 'react';
import { Link } from 'react-router-dom';
import { CaretLeft, CaretRight } from '@phosphor-icons/react';
import { NoteDocument } from '../../types/content';

interface PrevNextNavProps {
  prev: NoteDocument | null;
  next: NoteDocument | null;
}

export const PrevNextNav: React.FC<PrevNextNavProps> = ({ prev, next }) => {
  if (!prev && !next) return null;

  return (
    <nav
      aria-label="Previous and Next note navigation"
      className="prev-next-nav"
      style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
        gap: '14px',
        marginTop: '3.5rem',
        paddingTop: '2rem',
        borderTop: '1px solid var(--color-hairline)'
      }}
    >
      {prev ? (
        <Link
          to={prev.metadata.route}
          style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '6px',
            padding: '14px 16px',
            backgroundColor: 'var(--color-surface)',
            border: '1px solid var(--color-hairline)',
            borderRadius: 'var(--radius-md)',
            transition: 'all 0.15s ease'
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = 'var(--color-hairline-strong)';
            e.currentTarget.style.backgroundColor = 'var(--color-surface-elevated)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = 'var(--color-hairline)';
            e.currentTarget.style.backgroundColor = 'var(--color-surface)';
          }}
        >
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '12px', color: 'var(--color-mute)' }}>
            <CaretLeft size={12} /> Previous Note
          </span>
          <span style={{ fontSize: '14px', fontWeight: 500, color: 'var(--color-ink)' }}>
            {prev.metadata.title}
          </span>
        </Link>
      ) : (
        <div className="prev-nav-spacer" />
      )}

      {next ? (
        <Link
          to={next.metadata.route}
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'flex-end',
            textAlign: 'right',
            gap: '6px',
            padding: '14px 16px',
            backgroundColor: 'var(--color-surface)',
            border: '1px solid var(--color-hairline)',
            borderRadius: 'var(--radius-md)',
            transition: 'all 0.15s ease'
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.borderColor = 'var(--color-hairline-strong)';
            e.currentTarget.style.backgroundColor = 'var(--color-surface-elevated)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.borderColor = 'var(--color-hairline)';
            e.currentTarget.style.backgroundColor = 'var(--color-surface)';
          }}
        >
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '12px', color: 'var(--color-mute)' }}>
            Next Note <CaretRight size={12} />
          </span>
          <span style={{ fontSize: '14px', fontWeight: 500, color: 'var(--color-ink)' }}>
            {next.metadata.title}
          </span>
        </Link>
      ) : (
        <div className="next-nav-spacer" />
      )}

      <style>{`
        @media (max-width: 540px) {
          .prev-nav-spacer, .next-nav-spacer {
            display: none !important;
          }
          .prev-next-nav {
            grid-template-columns: 1fr !important;
          }
        }
      `}</style>
    </nav>
  );
};
