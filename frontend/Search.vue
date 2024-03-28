<template>
    <div class="home-link">
        <router-link to="/main"><i class="ri-arrow-left-line"></i></router-link>
    </div>
    <div class="container">
        <header>
            <h1>SEARCHING</h1>
        </header>
        <div class="form-container">
            <form>
                <input type="text" placeholder="Time">
                <input type="text" placeholder="Planet">
                <input type="text" placeholder="Doctor">
                <button class="btn-blue" @click.prevent="router.push('/character')">Search</button>
            </form>
            <div class="btn-white" @click.prevent="router.push('/history')">History</div>
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
    button {
        margin-top: 30px;
    }
 }
 .btn-white {
    margin-top: 45px;
 }
</style>