import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: ''
  }),
  actions: {
    setToken(token: string) {
      this.accessToken = token
    }
  }
})
