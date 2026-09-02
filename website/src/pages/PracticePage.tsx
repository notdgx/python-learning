import React from 'react';
import { Lightbulb } from '@phosphor-icons/react';
import { EmptyState } from '../components/common/EmptyState';

export const PracticePage: React.FC = () => {
  return (
    <div style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto', padding: 'clamp(32px, 5vw, 48px) clamp(16px, 3vw, 24px) 80px', width: '100%', overflowX: 'hidden' }}>
      <div style={{ marginBottom: '32px' }}>
        <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--color-mute)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          Exercises
        </span>
        <h1 style={{ fontSize: 'clamp(1.8rem, 5vw, 2.4rem)', color: 'var(--color-ink)', marginTop: '4px', marginBottom: '8px' }}>
          Practice & Interview Questions
        </h1>
        <p style={{ fontSize: '14.5px', color: 'var(--color-mute)', maxWidth: '650px', lineHeight: 1.6 }}>
          Curated practice questions, tricky Python puzzles, and structured problem walkthroughs.
        </p>
      </div>

      <EmptyState
        title="Practice Exercises Preparing"
        description="Structured practice problem sets and interactive challenge walkthroughs will be integrated into this section."
        actionText="Browse Knowledge Base"
        onAction={() => window.location.assign('/notes')}
        icon={<Lightbulb size={48} weight="thin" color="var(--color-stone)" />}
      />
    </div>
  );
};
