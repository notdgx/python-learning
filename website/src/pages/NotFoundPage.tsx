import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, House } from '@phosphor-icons/react';

export const NotFoundPage: React.FC = () => {
  return (
    <div
      style={{
        maxWidth: '600px',
        margin: '100px auto',
        padding: '0 24px',
        textAlign: 'center',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '20px'
      }}
    >
      <div style={{ fontSize: '4rem', fontWeight: 700, color: 'var(--color-ash)', fontFamily: 'var(--font-mono)' }}>
        404
      </div>
      <h1 style={{ fontSize: '1.8rem', color: 'var(--color-ink)' }}>Page Not Found</h1>
      <p style={{ fontSize: '15px', color: 'var(--color-mute)', lineHeight: 1.6, maxWidth: '440px' }}>
        The page or note you are looking for does not exist or has been moved.
      </p>
      <div style={{ display: 'flex', gap: '12px', marginTop: '12px' }}>
        <Link to="/" className="btn-primary">
          <House size={16} />
          <span>Go to Home</span>
        </Link>
        <Link to="/notes" className="btn-secondary">
          <ArrowLeft size={16} />
          <span>Browse Notes</span>
        </Link>
      </div>
    </div>
  );
};
