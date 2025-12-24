import { registerRootComponent } from 'expo'
import { HomeScreen } from 'app/features/home/screen'
import { TamaguiProvider, Theme } from 'tamagui'
import config from 'ui/src/tamagui.config'
import { useColorScheme } from 'react-native'

function App() {
  const colorScheme = useColorScheme()

  return (
    <TamaguiProvider config={config} defaultTheme={colorScheme === 'dark' ? 'dark' : 'light'}>
      <Theme name={colorScheme === 'dark' ? 'dark' : 'light'}>
        <HomeScreen />
      </Theme>
    </TamaguiProvider>
  )
}

registerRootComponent(App)







