<template>
  <div class="page">
    <form @submit.prevent="PostUser">
      <h1 id="loginH1">Вход</h1>
      <div class="input-box">
        <input type="email" placeholder="Email" v-model="email" required>
      </div>
      <div class="input-box">
        <input type="text" placeholder="Имя" v-model="nickname" required>
      </div>
      <div class="input-box">
        <input type="password" placeholder="Пароль" v-model="password" required>
      </div>
      <button @click="PostUser" class="btn">Вход</button>
      <!-- <input type="id" placeholder="ID" v-model="Id">
      <button @click="DeleteUser(Id)" class="btn">delete</button> -->
    </form>
  </div>
</template>

<script>
import axios from 'axios';

const debug = true;

export default {
  data() {
    return {
      Id: null,
      email: null,
      nickname: null,
      password: null,
      users: []
    }
  },
  methods: {
    async GetUsers() {
      const response = await axios.get("http://localhost:3000/api/users");
      this.users = response.data;
    },
    async PostUser() {
      await axios.post("http://localhost:3000/api/users", {
        email: this.email,
        nickname: this.nickname,
        password: this.password
      });
      if (debug == true) {
        console.log({
          email: this.email,
          nickname: this.nickname,
          password: this.password
        });
      }
      this.email = null;
      this.nickname = null;
      this.password = null;
    },
    async DeleteUser(userId) {
      await axios.delete("http://localhost:3000/api/users/" + userId);
      if (debug == true) console.log("User with ID " + userId + " deleted.");
    }
  }
}

</script>

<style>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-size: 25px;
}

body {
  display: flex;
  background: white;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

#loginH1 {
  margin-bottom: 20px;
  font-size: 30px;
  font-weight: 100;
  color: black;
  align-self: center;
}

.page {
  align-items: center;
  justify-content: center;
  display: flex;
  /* background: gray; */
  box-shadow: 0 0 3px 3px rgba(124, 119, 119, 0.363);
  border: 0.5px solid rgba(0, 0, 0, 0.548);
  border-radius: 20px;
  padding: 85px 40px 85px 40px;
}

.input-box input, .input-box:focus {
  outline: none;
  font-size: 22px;
  margin-top: 10px;
  margin-bottom: 15px;
  border: none;
  border-bottom: 0.5px solid rgba(133, 125, 125, 0.658);
}

.input-box input::placeholder {
  font-size: 20px;
  border-bottom: 2px solid rgba(133, 125, 125, 0.658);
  color: rgba(133, 125, 125, 0.658);
}

.btn {
  width: 100%;
  height: 35px;
  cursor: pointer;
  background: rgba(153, 153, 153, 0.699);
  border: none;
  border-radius: 20px;
  margin-top: 20px;
}

</style>