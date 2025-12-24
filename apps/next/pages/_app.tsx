import 'raf/polyfill'
import { NextThemeProvider, useRootTheme } from '@tamagui/next-theme'
import Head from 'next/head'
import React from 'react'
import { AppProps } from 'next/app'
import { TamaguiProvider } from 'tamagui'
import config from 'ui/src/tamagui.config'

export default function App({ Component, pageProps }: AppProps) {
  const [theme, setTheme] = useRootTheme()

  return (
    <>
      <Head>
        <title>M压轴</title>
        <meta name="description" content="初中数学压轴题 84个考法全覆盖" />
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
