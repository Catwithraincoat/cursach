<template>
    <div class="container">
        <div class="columns-2">
        <div class="img-container">
            <div class="img"></div>
            <div class="img-container__text">
                <h3>
                    The TARDIS isn't simply a gadget, it's a portal to the awe-inspiring wonders of the universe. A memorable journey awaits!
                </h3>
            </div>
        </div>
        <div class="form-container">
            <h1>Log In</h1>
            <form>
                <input type="text" placeholder="Login">
                <input type="password" placeholder="Password">
                <button class="btn-blue" @click.prevent="router.push('/main')">Go to the journey</button>
            </form>
        </div>
    </div>
    </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
</script>

<style lang="scss" scoped>
 h1 {
    color: #fff;
    font-size: 3em;
 }
 .form-container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
    input {
        width: 400px;
        height: 80px;
        border-radius: 10px;
        text-align: center;
        text-transform: uppercase;
        font-size: 1em;
        outline: none;
        border: none;
    }
    button {
        margin-top: 30px;
    }
 }
 .img {
    width: 450px;
    height: 450px;
    margin-bottom: 15px;
 }
 .img-container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
 }
 h3 {
    font-weight: 400;
    font-size: 1.6em;
 }
</style>