<template>
    <div class="home-link">
        <router-link to="/main"><i class="ri-arrow-left-line"></i></router-link>
    </div>
    <div class="container">
        <header>
            <h1>Current HISTORY</h1>
        </header>
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>NO</th>
                        <th>Time</th>
                        <th>Planet</th>
                        <th>Doctor</th>
                        <th>Deccription</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>12345</td>
                        <td>1963-Present</td>
                        <td>Galifrey</td>
                        <td>Doctor</td>
                        <td>Someone died</td>
                    </tr>
                    <tr>
                        <td>12345</td>
                        <td>1963-Present</td>
                        <td>Galifrey</td>
                        <td>Doctor</td>
                        <td>Someone died</td>
                    </tr>
                    <tr>
                        <td>12345</td>
                        <td>1963-Present</td>
                        <td>Galifrey</td>
                        <td>Doctor</td>
                        <td>Someone died</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="btn-container">
            <div class="btn-blue" @click="router.push('/search')">Search for more</div>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
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