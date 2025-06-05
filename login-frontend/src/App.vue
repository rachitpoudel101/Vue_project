<!-- src/App.vue -->
<template>
  <div id="app">
    <!-- Remove or replace <HelloWorld /> if you don’t need it -->
    <!-- <HelloWorld msg="Welcome" /> -->
    <Signup />
    <UserList />
  </div>
</template>

<script>
import Signup from './components/Signup.vue'
import UserList from './components/UserList.vue'
// import HelloWorld from './components/HelloWorld.vue'  // 🔴 Remove this line
// import TheWelcome from './components/TheWelcome.vue'  // Also remove if unused

export default {
  components: {
    Signup,
    UserList,
    // HelloWorld,
    // TheWelcome
  }
}
</script>
