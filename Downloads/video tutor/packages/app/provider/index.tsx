import { SafeArea } from 'app/provider/safe-area'
import { NavigationProvider } from './navigation'
import { TamaguiProvider, config } from '@my/ui'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { useState } from 'react'

export function Provider({ children }: { children: React.ReactNode }) {
  const [queryClient] = useState(() => new QueryClient())

  return (
    <TamaguiProvider config={config} defaultTheme="light">
      <QueryClientProvider client={queryClient}>
        <SafeArea>
          <NavigationProvider>{children}</NavigationProvider>
        </SafeArea>
      </QueryClientProvider>
    </TamaguiProvider>
  )
}
