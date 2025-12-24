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
    return (
      <Html lang="zh-CN">
        <Head>
          <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}
