<template>
    <div class="home-link">
        <router-link to="/main"><i class="ri-arrow-left-line"></i></router-link>
    </div>
    <div class="container">
        <header>
            <h1>Messages</h1>
        </header>
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>NO</th>
                        <th>Time</th>
                        <th>From</th>
                        <th>MESSAGE</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>12345</td>
                        <td>1963-Present</td>
                        <td>Dalecks</td>
                        <td>lalalalalallalallllllallalalallalallallalallalallalal</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="btn-container">
            <router-link to="/msg-page" class="btn-blue">Write a message</router-link>
        </div>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>
 h1 {
    font-size: 8em;
    text-align: center;
 }
 .btn-container {
    display: flex;
    max-width: 1200px;
    width: 100%;
    justify-content: center;
    align-items: center;
    margin-top: 60px;
 }
</style>