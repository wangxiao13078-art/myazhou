module.exports = function (api) {
  api.cache(true)
  return {
    presets: [['babel-preset-expo', { jsxRuntime: 'automatic' }]],
    plugins: [
      [
        '@tamagui/babel-plugin',
        {
          config: '../../packages/ui/src/tamagui.config.ts',
          components: ['tamagui'],
        },
      ],
      'react-native-reanimated/plugin',
    ],
  }
}







