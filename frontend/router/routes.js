export default [
    {
        path: '/',
        name: 'welcome',
        component: () => import('../pages/Welcome.vue'),
    },
    {
        path: '/main',
        name: 'main',
        component: () => import('../pages/Main.vue'),
    },
    {
        path: '/signup',
        name: 'signup',
        component: () => import('../pages/Signup.vue'),
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../pages/Login.vue'),
    },
    {
        path: '/account',
        name: 'account',
        component: () => import('../pages/Account.vue'),
    },
    {
        path: '/recent',
        name: 'recent',
        component: () => import('../pages/Recent.vue'),
    },
    {
        path: '/msg',
        name: 'msg',
        component: () => import('../pages/Msg.vue'),
    },
    {
        path: '/battles',
        name: 'battles',
        component: () => import('../pages/Battles.vue'),
    },
    {
        path: '/msg-page',
        name: 'msg-page',
        component: () => import('../pages/Msg-page.vue'),
    },
    {
        path: '/search',
        name: 'search',
        component: () => import('../pages/Search.vue'),
    },
    {
        path: '/history',
        name: 'history',
        component: () => import('../pages/History.vue'),
    },
    {
        path: '/character',
        name: 'character',
        component: () => import('../pages/Character.vue'),
    },
];
