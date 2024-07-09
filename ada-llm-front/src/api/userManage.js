import request from '@/utils/request'
// import axios from "axios";

export default {
  getUserList(searchModel){
    return request({
      url: '/user/list',
      method: 'get',
      params:{
        pageNo: searchModel.pageNo,
        pageSize: searchModel.pageSize,
        username: searchModel.username,
        phone: searchModel.phone,
        email: searchModel.email
      }
    })
  },

  addUser(user){
    return request({
      url: '/user',
      method: 'post',
      data: user
    });
  },

  updateUser(user){
    return request({
      url: '/user',
      method: 'put',
      data: user
    });
  },

  saveUser(user){
    if(user.id == null || user.id == 'defined'){
      return this.addUser(user);
    }else{
      return this.updateUser(user);
    }
  },

  getUserById(id){
    return request({
      // url: '/user/'+id,
      url: `/user/${id}`,
      method: 'get'
    });
  },

  deleteUserById(id){
    return request({
      url: `/user/${id}`,
      method: 'delete'
    });
  },

  register(user){
    return request({
      url: '/user/register',
      method: 'post',
      data: user
    });
  },

  getFileList() {
    return request({
      url: '/userFile/list',
      method: 'get'
    });
  },



}
