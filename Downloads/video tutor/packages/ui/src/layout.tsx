import { YStack, XStack, styled } from 'tamagui'

export const PageContainer = styled(YStack, {
  flex: 1,
  padding: '$4',
  backgroundColor: '$background',
})

export const Row = styled(XStack, {
  alignItems: 'center',
  gap: '$2',
})

export const Center = styled(YStack, {
  alignItems: 'center',
  justifyContent: 'center',
})

