import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { GithubLogo, List, X, Star, CurrencyInr } from '@phosphor-icons/react';
import { LinksDropdown } from './LinksDropdown';

interface NavbarProps {
  onOpenDonate: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ onOpenDonate }) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const location = useLocation();

  const navLinks = [
    { label: 'Home', path: '/' },
    { label: 'Notes', path: '/notes' },
    { label: 'Projects', path: '/projects' },
    { label: 'Practice', path: '/practice' }
  ];

  const isActive = (path: string) => {
    if (path === '/') return location.pathname === '/';
    return location.pathname.startsWith(path);
  };

  return (
    <header
      style={{
        position: 'sticky',
        top: 0,
        zIndex: 500,
        height: 'var(--navbar-height)',
        backgroundColor: 'rgba(5, 5, 5, 0.85)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        borderBottom: '1px solid var(--color-hairline)',
        display: 'flex',
        alignItems: 'center'
      }}
    >
      <div
        style={{
          width: '100%',
          maxWidth: 'var(--max-content-width)',
          margin: '0 auto',
          padding: '0 24px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between'
        }}
      >
        {/* Left: Brand Identity */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '32px' }}>
          <Link to="/" className="site-title" aria-label="python-learning homepage">
            python-learning
          </Link>

          {/* Desktop Nav Links */}
          <nav
            style={{
              display: 'none',
              alignItems: 'center',
              gap: '4px'
            }}
            className="desktop-nav"
          >
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                style={{
                  fontSize: '14px',
                  fontWeight: 500,
                  padding: '6px 12px',
                  borderRadius: 'var(--radius-sm)',
                  color: isActive(link.path) ? 'var(--color-on-dark)' : 'var(--color-body)',
                  backgroundColor: isActive(link.path) ? 'var(--color-surface-elevated)' : 'transparent',
                  transition: 'all 0.15s ease'
                }}
              >
                {link.label}
              </Link>
            ))}
            <LinksDropdown onOpenDonate={onOpenDonate} />
          </nav>
        </div>

        {/* Right: Actions */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          {/* GitHub Star Badge */}
          <a
            href="https://github.com/notdgx/python-learning"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '6px 10px',
              backgroundColor: 'var(--color-surface-elevated)',
              border: '1px solid var(--color-hairline)',
              borderRadius: 'var(--radius-md)',
              fontSize: '13px',
              color: 'var(--color-ink)',
              transition: 'border-color 0.15s ease'
            }}
            aria-label="GitHub Repository"
          >
            <GithubLogo size={16} />
            <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px', color: 'var(--color-mute)', fontSize: '12px' }}>
              <Star size={12} weight="fill" color="var(--color-mute)" />
              <span>Star</span>
            </span>
          </a>

          {/* Donate CTA */}
          <button
            onClick={onOpenDonate}
            className="btn-primary"
            style={{ height: '32px', padding: '0 14px', fontSize: '13px', display: 'inline-flex', alignItems: 'center', gap: '4px' }}
          >
            <CurrencyInr size={15} weight="bold" />
            <span>Donate</span>
          </button>

          {/* Mobile Menu Toggle */}
          <button
            type="button"
            onClick={() => setMobileMenuOpen((prev) => !prev)}
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '6px',
              color: 'var(--color-ink)',
              borderRadius: 'var(--radius-sm)'
            }}
            className="mobile-menu-btn"
            aria-label={mobileMenuOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={mobileMenuOpen}
          >
            {mobileMenuOpen ? <X size={22} /> : <List size={22} />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div
          style={{
            position: 'fixed',
            top: 'var(--navbar-height)',
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: 'rgba(5, 5, 5, 0.98)',
            backdropFilter: 'blur(20px)',
            padding: '24px',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px',
            zIndex: 499,
            overflowY: 'auto'
          }}
          className="mobile-drawer"
        >
          {navLinks.map((link) => (
            <Link
              key={link.path}
              to={link.path}
              onClick={() => setMobileMenuOpen(false)}
              style={{
                fontSize: '18px',
                fontWeight: 500,
                padding: '12px 16px',
                borderRadius: 'var(--radius-md)',
                color: isActive(link.path) ? 'var(--color-on-dark)' : 'var(--color-mute)',
                backgroundColor: isActive(link.path) ? 'var(--color-surface)' : 'transparent'
              }}
            >
              {link.label}
            </Link>
          ))}
          <Link
            to="/links"
            onClick={() => setMobileMenuOpen(false)}
            style={{
              fontSize: '18px',
              fontWeight: 500,
              padding: '12px 16px',
              borderRadius: 'var(--radius-md)',
              color: 'var(--color-mute)'
            }}
          >
            Links Directory
          </Link>
          <button
            onClick={() => {
              setMobileMenuOpen(false);
              onOpenDonate();
            }}
            style={{
              marginTop: '12px',
              width: '100%',
              height: '44px',
              backgroundColor: 'var(--color-surface-elevated)',
              border: '1px solid var(--color-hairline)',
              borderRadius: 'var(--radius-md)',
              color: 'var(--color-ink)',
              fontSize: '16px',
              fontWeight: 500
            }}
          >
            Donate via UPI
          </button>
        </div>
      )}

      <style>{`
        @media (min-width: 768px) {
          .desktop-nav {
            display: flex !important;
          }
          .mobile-menu-btn {
            display: none !important;
          }
          .mobile-drawer {
            display: none !important;
          }
        }
      `}</style>
    </header>
  );
};
