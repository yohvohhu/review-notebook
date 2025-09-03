<template>
  <div class="login">
    <el-form @submit.prevent="login">
      <el-form-item label="Email">
        <el-input v-model="email" />
      </el-form-item>
      <el-form-item label="Password">
        <el-input v-model="password" type="password" />
      </el-form-item>
      <el-button type="primary" @click="login">Login</el-button>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const store = useAuthStore()
const router = useRouter()

async function login() {
  const params = new URLSearchParams()
  params.append('username', email.value)
  params.append('password', password.value)
  const res = await axios.post('/api/auth/login', params)
  store.setToken(res.data.access_token)
  router.push('/review')
}
</script>
