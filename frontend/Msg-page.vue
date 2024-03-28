<template>
    <div class="home-link">
        <router-link to="/main"><i class="ri-arrow-left-line"></i></router-link>
    </div>
    <div class="container">
        <header>
            <h1>Message</h1>
        </header>
        <div class="form-container">
            <form>
                <input type="text" placeholder="Time">
                <input type="text" placeholder="User">
                <textarea name="description" contenteditable="true" placeholder="Write here"></textarea>
                <button class="btn-blue" @click.prevent="router.push('/msg')">Send</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
</script>

<style lang="scss" scoped>
 h1 {
    font-size: 5em;
    text-align: center;
 }
 .form-container {
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
    textarea {
        width: 400px;
        border-radius: 10px;
        padding: 15px;
        box-sizing: border-box;
        border: none;
        font-size: 1em;
        text-align: center;
        outline: none;
        max-width: 400px;
        min-width: 400px;
        height: 300px;
        max-height: 300px;
        min-height: 300px;
    }
    button {
        margin-top: 30px;
    }
 }
</style>