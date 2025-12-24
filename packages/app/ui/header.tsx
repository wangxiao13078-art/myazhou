import React, { useEffect, useState } from 'react'
import { XStack, Text, Button } from 'tamagui'
import { ChevronLeft, Sun, Moon } from '@tamagui/lucide-icons'
import { useRouter } from 'solito/router'
import { useThemeSetting } from '@tamagui/next-theme'

interface HeaderProps {
  title: string
  showBack?: boolean
}

export function Header({ title, showBack }: HeaderProps) {
  const { back } = useRouter()
  const { current, set } = useThemeSetting()
  const [mounted, setMounted] = useState(false)
  
  useEffect(() => {
    setMounted(true)
  }, [])
  
  const toggleTheme = () => {
    set(current === 'light' ? 'dark' : 'light')
  }

  return (
    <XStack 
      height={54} 
      alignItems="center" 
      justifyContent="space-between" 
      px="$4" 
      backgroundColor="$background"
      borderBottomWidth={1}
      borderBottomColor="$borderColor"
      // @ts-ignore - sticky is valid CSS
      position="sticky"
      top={0}
      zIndex={100}
    >
      <XStack width={80} alignItems="center">
        {showBack && (
          <Button 
            icon={ChevronLeft} 
            chromeless 
            onPress={() => back()} 
            p={0}
            scaleIcon={1.5}
          />
        )}
      </XStack>

      <Text fontWeight="bold" fontSize="$5" color="$color" textAlign="center" f={1} numberOfLines={1}>
        {title}
      </Text>

      <XStack width={80} justifyContent="flex-end" ai="center" space="$2">
        {mounted && (
          <Button
            icon={current === 'light' ? Sun : Moon}
            chromeless
            onPress={toggleTheme}
            p="$2"
            scaleIcon={1.2}
          />
        )}
      </XStack>
    </XStack>
  )
}
