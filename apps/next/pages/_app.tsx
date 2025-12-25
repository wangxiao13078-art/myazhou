import 'raf/polyfill'
import { NextThemeProvider, useRootTheme } from '@tamagui/next-theme'
import Head from 'next/head'
import React, { useEffect } from 'react'
import { AppProps } from 'next/app'
import { TamaguiProvider } from 'tamagui'
import config from 'ui/src/tamagui.config'

// 注册 Service Worker
function useServiceWorker() {
  useEffect(() => {
    if (typeof window !== 'undefined' && 'serviceWorker' in navigator) {
      const basePath = window.location.hostname.includes('github.io') ? '/myazhou' : ''
      
      navigator.serviceWorker
        .register(`${basePath}/sw.js`)
        .then((registration) => {
          console.log('Service Worker 注册成功:', registration.scope)
        })
        .catch((error) => {
          console.log('Service Worker 注册失败:', error)
        })
    }
  }, [])
}

export default function App({ Component, pageProps }: AppProps) {
  const [theme, setTheme] = useRootTheme()
  
  // 注册 PWA Service Worker
  useServiceWorker()

  return (
    <>
      <Head>
        <title>七年级数学压轴题</title>
        <meta name="description" content="七年级数学期末压轴题训练 - 84个考法全覆盖" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <NextThemeProvider onChangeTheme={(next) => setTheme(next as any)}>
        <TamaguiProvider config={config} disableInjectCSS defaultTheme={theme}>
          <Component {...pageProps} />
        </TamaguiProvider>
      </NextThemeProvider>
    </>
  )
}
