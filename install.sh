kubectl run print-request --image=reaper7/print-request:v1 -l app=print-request-v1  --env="HTTP_SERVER_TIMEOUT=0"
kubectl expose pod print-request --port=3000 --name=print-request -l app=print-request-v1
kubectl create ing print-request --rule="${ING_HOST}/print-request*=print-request:3000" --class="${ING_CLASS}"