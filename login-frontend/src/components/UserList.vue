<template>
  <div>
    <h2>Users</h2>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.username }} — {{ user.password }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      users: []
    }
  },
  mounted() {
    axios.get('http://localhost:8000/api/users/')
      .then(response => {
        this.users = response.data
      })
      .catch(() => {
        alert('Failed to fetch users')
      })
  }
}
</script>
