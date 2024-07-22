import { createRouter, createWebHistory, type RouteRecordRaw, type Router } from 'vue-router'

// 定义静态路由（constantRoutes）
export const constantRoutes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login/MyLogin.vue')
  },
  {
    path: '/',
    redirect: 'login'
  },
  {
    path: '/chat',
    name: 'chat',
    component: () => import('@/views/ChatWindow/Chat.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('@/views/TestView.vue')
  }
  // 其他静态路由
]

const createRouterInstance = () => createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: constantRoutes
})

// 创建初始路由实例
let router: Router = createRouterInstance()

// 重置路由的函数
export function resetRouter() {
  const newRouter = createRouterInstance()
  router.options.routes = newRouter.options.routes
}

export default router
