import request from '@/utils/request'

export function sendPromptMessage(data) {
  return request({
    url: '/api/rag',
    method: 'post',
    data
  });
}
