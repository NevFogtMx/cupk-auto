<template>
  <div style="margin: 22% auto;">
      <el-select v-model="value" class="m-2" placeholder="Select" size="large" @change="handleChange">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
          </el-select><br><br>
      <div v-if="value == 2" class="captcha">
          <el-image :src="url" fit='scale-down' title="验证码" @click="changeCaptcha">
            <template #error>
                loading...
            </template>
          </el-image>
          <el-input v-model="captcha" placeholder="输入验证码" class="w-100" clearable />
      </div>
      
      <br>
      <el-button class="login-btn" type="primary" size="large" round @click="handleClick">登录</el-button>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { ElMessage, ElLoading } from 'element-plus'
import { useRouter } from 'vue-router'


const value = ref(1)
const router = useRouter()
const data = ref({})
const url = ref('')
const captcha = ref('')

const options = [{
  "value": 1,
  "label": "教务系统"
},{
  "value": 2,
  "label": "融合门户"
}]

function handleChange(val){
    if(val == 2){
        fetch("http://localhost:8877/rhmh/login/getCaptcha").then(res=>res.json())
        .then(res=>{
          data.value = res.data
          url.value = res.data.captcha
        }).catch(err=>{
          console.log(err)
        })
    }
}

function changeCaptcha(){
  fetch("http://localhost:8877/rhmh/login/changeCaptcha").then(res=>res.json())
  .then(res=>{
    if(res.code == 1){
        url.value = res.data.captcha
    }else{
        ElMessage.error("验证码刷新失败")
    }
  }).catch(err=>{
    console.log(err)
  })
}

function handleClick() {
  const loading = ElLoading.service({
    lock: true,
    text: '登录中...',
    background: 'rgba(0, 0, 0, 0.7)',
  })
  if(value.value === 1){
      // 登录教务系统
      fetch("http://localhost:8877/jwxt/login").then(res=>res.json())
      .then(res=>{
        loading.close()
          if(res.code === 1){
              ElMessage({
                  message: '登录成功',
                  type: 'success'
              })
              router.push({path: "/sis/home/qk"})
          }else{
              ElMessage.error(res.msg)
          }
      })
      .catch(err=>{
        console.log(err)
      })
  }else if(value.value === 2){
    // 登录融合门户
    data.value.captcha = captcha.value
      fetch("http://localhost:8877/rhmh/login",{
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data.value)
      }).then(res=>res.json())
      .then(res=>{
          loading.close()
          if(res.code === 1){
              ElMessage({
                  message: '登录成功',
                  type: 'success'
              });
              router.push({path: "/fp/home/main"})
          }else{
              ElMessage.error(res.msg)
          }
      })
      .catch(err=>{
        console.log(err)
      })
  }
}

</script>

<style scoped>
.w-100{
  margin-left: 20px;
  width: 200px;
}
.captcha{
  display: flex;
  align-items: center;
  justify-content: center;
}
.captcha .el-image{
  height: 25px;
  width: 80px;
}
.captcha .el-image:hover{
  cursor: pointer;
}
.login-btn{
  width: 150px;
}
</style>
