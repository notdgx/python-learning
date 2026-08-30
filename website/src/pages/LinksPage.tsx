import React from 'react';
import {
  YoutubeLogo,
  InstagramLogo,
  XLogo,
  GithubLogo,
  EnvelopeSimple,
  ArrowSquareOut,
  Book,
  Code
} from '@phosphor-icons/react';

export const LinksPage: React.FC = () => {
  const resourceCategories = [
    {
      title: 'Creator & Social Links',
      description: 'Official profiles and community channels for notdgx.',
      items: [
        {
          name: 'notdgx on GitHub',
          handle: '@notdgx',
          url: 'https://github.com/notdgx/',
          icon: <GithubLogo size={22} />,
          desc: 'Open-source repositories, developer tools, and projects.'
        },
        {
          name: 'notdgx on YouTube',
          handle: '@notdgx',
          url: 'https://www.youtube.com/@notdgx',
          icon: <YoutubeLogo size={22} />,
          desc: 'Technical tutorials, deep dives, and programming demonstrations.'
        },
        {
          name: 'howdgx on YouTube',
          handle: '@howdgx',
          url: 'https://www.youtube.com/@howdgx',
          icon: <YoutubeLogo size={22} />,
          desc: 'Behind the scenes, developer logs, and technical explorations.'
        },
        {
          name: 'notdgx on Instagram',
          handle: '@notdgx',
          url: 'https://www.instagram.com/notdgx',
          icon: <InstagramLogo size={22} />,
          desc: 'Visual notes, programming snippets, and developer updates.'
        },
        {
          name: 'howdgx on Instagram',
          handle: '@howdgx',
          url: 'https://www.instagram.com/howdgx',
          icon: <InstagramLogo size={22} />,
          desc: 'Tech lifestyle, workspace setups, and behind-the-scenes logs.'
        },
        {
          name: 'notdgx on X (Twitter)',
          handle: '@notdgxsh',
          url: 'https://x.com/notdgxsh',
          icon: <XLogo size={22} />,
          desc: 'Thoughts on software architecture, performance, and tooling.'
        },
        {
          name: 'Contact & Support Email',
          handle: 'howdgx@gmail.com',
          url: 'mailto:howdgx@gmail.com',
          icon: <EnvelopeSimple size={22} />,
          desc: 'Direct email inquiries for feedback, collaborations, or questions.'
        }
      ]
    },
    {
      title: 'Python Ecosystem & References',
      description: 'Official documentation and standards.',
      items: [
        {
          name: 'Official Python 3 Documentation',
          handle: 'docs.python.org/3',
          url: 'https://docs.python.org/3/',
          icon: <Book size={22} />,
          desc: 'Complete official standard library, tutorial, and language reference.'
        },
        {
          name: 'CPython GitHub Repository',
          handle: 'github.com/python/cpython',
          url: 'https://github.com/python/cpython',
          icon: <Code size={22} />,
          desc: 'The reference C implementation of the Python programming language.'
        }
      ]
    }
  ];

  return (
    <div style={{ maxWidth: 'var(--max-content-width)', margin: '0 auto', padding: '48px 24px 80px', width: '100%' }}>
      <div style={{ marginBottom: '36px' }}>
        <span style={{ fontSize: '12px', fontWeight: 600, color: 'var(--color-mute)', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          Directory
        </span>
        <h1 style={{ fontSize: '2.4rem', color: 'var(--color-ink)', marginTop: '4px', marginBottom: '8px' }}>
          Resources & Links
        </h1>
        <p style={{ fontSize: '15px', color: 'var(--color-mute)', maxWidth: '650px' }}>
          Curated directory of creator channels, community profiles, official Python resources, and repositories.
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '48px' }}>
        {resourceCategories.map((cat, idx) => (
          <div key={idx} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div>
              <h2 style={{ fontSize: '1.4rem', color: 'var(--color-ink)', marginBottom: '4px' }}>
                {cat.title}
              </h2>
              <p style={{ fontSize: '13.5px', color: 'var(--color-mute)' }}>
                {cat.description}
              </p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '16px' }}>
              {cat.items.map((item, itemIdx) => (
                <a
                  key={itemIdx}
                  href={item.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="surface-card"
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between',
                    gap: '16px',
                    padding: '20px'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                      <div
                        style={{
                          width: '40px',
                          height: '40px',
                          borderRadius: 'var(--radius-md)',
                          backgroundColor: 'var(--color-surface-card)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          color: 'var(--color-ink)'
                        }}
                      >
                        {item.icon}
                      </div>
                      <div>
                        <h3 style={{ fontSize: '14.5px', color: 'var(--color-ink)', fontWeight: 500 }}>
                          {item.name}
                        </h3>
                        <span style={{ fontSize: '12px', color: 'var(--color-mute)', fontFamily: 'var(--font-mono)' }}>
                          {item.handle}
                        </span>
                      </div>
                    </div>
                    <ArrowSquareOut size={16} color="var(--color-mute)" />
                  </div>

                  <p style={{ fontSize: '13px', color: 'var(--color-mute)', lineHeight: 1.5 }}>
                    {item.desc}
                  </p>
                </a>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
