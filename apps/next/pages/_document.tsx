import React from 'react'
import Document, { Html, Head, Main, NextScript, DocumentContext } from 'next/document'
import { AppRegistry } from 'react-native-web'
import config from 'ui/src/tamagui.config'

export default class MyDocument extends Document {
  static async getInitialProps(ctx: DocumentContext) {
    AppRegistry.registerComponent('Main', () => Main)
    // @ts-ignore
    const { getStyleElement } = AppRegistry.getApplication('Main')
    
    const page = await ctx.renderPage()
    const initialProps = await Document.getInitialProps(ctx)
    
    const styles = [
      <style
        key="tamagui-css"
        dangerouslySetInnerHTML={{
          __html: config.getCSS(),
        }}
      />,
      getStyleElement(),
    ]

    return { ...initialProps, ...page, styles: React.Children.toArray(styles) }
  }

  render() {
    const basePath = process.env.NODE_ENV === 'production' ? '/myazhou' : ''
    
    return (
      <Html lang="zh-CN">
        <Head>
          <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
          
          {/* PWA 配置 */}
          <link rel="manifest" href={`${basePath}/manifest.json`} />
          <meta name="theme-color" content="#4f46e5" />
          <meta name="apple-mobile-web-app-capable" content="yes" />
          <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
          <meta name="apple-mobile-web-app-title" content="数学压轴" />
          
          {/* 图标 */}
          <link rel="icon" type="image/png" sizes="192x192" href={`${basePath}/icons/icon-192.png`} />
          <link rel="apple-touch-icon" href={`${basePath}/icons/icon-192.png`} />
          
          {/* 防止自动检测电话号码 */}
          <meta name="format-detection" content="telephone=no" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}
