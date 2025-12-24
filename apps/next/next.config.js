/** @type {import('next').NextConfig} */
const { withTamagui } = require('@tamagui/next-plugin')

let nextConfig = {
  reactStrictMode: true,
  transpilePackages: [
    'react-native-web',
    'react-native-svg',
    '@react-native/assets-registry',
    'solito',
    'moti',
    'app',
    'lucide-react-native',
  ],
  experimental: {
    scrollRestoration: true,
  },
}

const plugins = [
  withTamagui({
    config: '../../packages/ui/src/tamagui.config.ts',
    components: ['tamagui'],
    importsWhitelist: ['constants.js', 'colors.js'],
    logTimings: true,
    disableExtraction: process.env.NODE_ENV === 'development',
  }),
]

module.exports = function () {
  for (const plugin of plugins) {
    nextConfig = plugin(nextConfig)
  }
  
  const webpack = nextConfig.webpack
  nextConfig.webpack = (config, options) => {
    if (webpack) {
      config = webpack(config, options)
    }
    config.resolve.alias = {
      ...(config.resolve.alias || {}),
      'react-native-svg': 'react-native-svg-web',
    }
    return config
  }
  
  return nextConfig
}
