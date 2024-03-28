<template>
    <div class="home-link">
        <router-link to="/main"><i class="ri-arrow-left-line"></i></router-link>
    </div>
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
        <div class="data-container">
            <h1>Name</h1>
            <div class="user-data">
                <div class="user-data__item">Race</div>
                <div class="user-data__item">Decription_of_character</div>
                <div class="user-data__item">login</div>
                <button class="btn-blue" @click.prevent="router.push('/main')">Log out</button>
            </div>
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
 .data-container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    .user-data {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
    .user-data__item {
        width: 400px;
        height: 100px;
        border-radius: 10px;
        text-transform: uppercase;
        font-size: 1em;
        outline: none;
        background: #fff;
        color: #858383;
        display: flex;
        justify-content: center;
        align-items: center;
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