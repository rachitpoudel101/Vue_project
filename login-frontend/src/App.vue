<template>
  <div id="app">
    <Signup />
    <UserList />
  </div>
</template>

<script>
import Signup from './components/Signup.vue'
import UserList from './components/UserList.vue'


export default {
  components: {
    Signup,
    UserList,

  }
}
</script>
