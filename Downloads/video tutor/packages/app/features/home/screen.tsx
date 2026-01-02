'use client'

import Link from 'next/link'

export function HomeScreen() {
  return (
    <div style={styles.container}>
      <div style={styles.content}>
        <h1 style={styles.title}>Video Tutor</h1>
        <p style={styles.subtitle}>
          Upload a math problem and watch it being solved on an animated whiteboard.
        </p>
        <Link href="/tutor" style={styles.link}>
          <button style={styles.button}>Start Tutoring</button>
        </Link>
      </div>
    </div>
  )
}

const styles: Record<string, React.CSSProperties> = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
    backgroundColor: '#fafafa',
    fontFamily: 'system-ui, -apple-system, sans-serif',
  },
  content: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: 24,
    maxWidth: 500,
    textAlign: 'center',
  },
  title: {
    fontSize: 42,
    fontWeight: 800,
    color: '#1a1a1a',
    margin: 0,
  },
  subtitle: {
    fontSize: 18,
    color: '#6b7280',
    lineHeight: 1.6,
    margin: 0,
  },
  link: {
    textDecoration: 'none',
  },
  button: {
    padding: '16px 32px',
    fontSize: 18,
    fontWeight: 600,
    backgroundColor: '#4f46e5',
    color: 'white',
    border: 'none',
    borderRadius: 10,
    cursor: 'pointer',
    transition: 'background-color 0.2s',
  },
}
