<template>
    <main>
        <div class="container">
            <h2><router-link to="/account">Hello &lt;Character_name&gt;</router-link></h2>
            <h1>
                Meet the Extraordinary <br>
                Individuals who've braved the <br>
                unknown with tardis, each <br>
                making their unique mark on the <br>
                story line.
            </h1>
            <div class="link-container">
                <router-link to="/recent" class="nav-link">
                    <div class="nav-img"></div>
                    <div class="nav-text">
                        <span class="nav-title">Time Travels</span>
                        <span class="nav-excerpt">Hundreds of Epochs Visited</span>
                    </div>
                    <div class="nav-arrow">
                        <i class="ri-arrow-right-s-line"></i>
                    </div>
                </router-link>
                <router-link to="/msg" class="nav-link">
                    <div class="nav-img"></div>
                    <div class="nav-text">
                        <span class="nav-title">Messages</span>
                        <span class="nav-excerpt">Countless words and invitations</span>
                    </div>
                    <div class="nav-arrow">
                        <i class="ri-arrow-right-s-line"></i>
                    </div>
                </router-link>
                <router-link to="/battles" class="nav-link">
                    <div class="nav-img"></div>
                    <div class="nav-text">
                        <span class="nav-title">Battles</span>
                        <span class="nav-excerpt">Destroy or save the univese</span>
                    </div>
                    <div class="nav-arrow">
                        <i class="ri-arrow-right-s-line"></i>
                    </div>
                </router-link>
            </div>
        </div>
    </main>
</template>

<script setup>

</script>

<style lang="scss" scoped>
.container {
    padding-bottom: 60px;
}
h2 {
    font-size: 1em;
    font-weight: 400;
}
h1 {
    font-size: 4em;
    line-height: 1.1em;
}
.link-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.nav-link {
    background: #0D0D0D;
    padding: 20px;
    border-radius: 20px;
    max-width: 1200px;
    width: 100%;
    color: #fff;
    display: flex;
    align-items: center;
    box-sizing: border-box;
}
.nav-text {
    display: flex;
    flex-direction: column;
    width: 950px;
}
.nav-title {
    font-size: 1.2em;
}
.nav-excerpt {
    font-size: .95em;
}
.nav-img {
    height: 120px;
    width: 120px;
    margin-right: 30px;
}
.nav-arrow {
    width: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2.5em;
}
</style>