<template>
  <form @submit.prevent="signup">
    <input v-model="username" placeholder="Username" required />
    <input v-model="password" type="password" placeholder="Password" required />
    <button type="submit">Sign Up</button>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async signup() {
      try {
        await axios.post('http://localhost:8000/api/register/', {
          username: this.username,
          password: this.password
        })
        alert('User registered!')
      } catch (error) {
        alert('Registration failed')
      }
    }
  }
}
</script>
