<template>
    <main>
        <div class="container welcome-container">
            <h1>Dive into the Cosmic Voyage</h1>
            <div class="btn-container">
                <router-link to="/signup" class="btn-white">Sign Up</router-link>
                <router-link to="/login" class="btn-blue">Log In</router-link>
            </div>
        </div>
    </main>
</template>

<script setup>

</script>

<style lang="scss" scoped>
h1 {
    font-size: 8em;
    text-align: center;
    line-height: 1.1em;
}
.welcome-container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
.btn-container {
    display: flex;
    gap: 10px;
    font-weight: 700;
}
</style>