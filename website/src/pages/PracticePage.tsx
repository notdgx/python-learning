import React from 'react';
import { Lightbulb } from '@phosphor-icons/react';
import { EmptyState } from '../components/common/EmptyState';

export const PracticePage: React.FC = () => {
  return (
    <div style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto', padding: '48px 24px 80px', width: '100%' }}>
      <div style={{ marginBottom: '36px' }}>
        <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--color-mute)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          Exercises
        </span>
        <h1 style={{ fontSize: '2.4rem', color: 'var(--color-ink)', marginTop: '4px', marginBottom: '8px' }}>
          Practice & Interview Questions
        </h1>
        <p style={{ fontSize: '15px', color: 'var(--color-mute)', maxWidth: '650px' }}>
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
