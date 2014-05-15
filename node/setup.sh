#!/bin/bash

here="$(cd "${0%/*}"; pwd)"

source $here/config.sh


if [ $1 ]; then
  option=$1
else
  option="default"
fi

setup () {
  dir=$1
  cd $dir
  virtualenv venv
  source ./venv/bin/activate
  if [[ -f requirements.txt ]]; then
    pip_req="requirements.txt"
  elif [[ -f pip-req.txt ]]; then
    pip_req="pip-req.txt"
  fi
  if [ $pip_req ]; then
    pip install -r $pip_req
  fi
  echo $pip_req
  pip install -e .
}

setup_dir () {
  folder=$1
  for file in "$folder"/*; do
    if [[ -d $file ]]; then
      project_name="$(basename "$file")"
      echo "setup $project_name ..."

      setup $file
    fi
  done
}

init () {
  setup_dir $here
}

run_git_rpc_server () {
  source ./jagare-rpc/venv/bin/activate

  python ./jagare-rpc/devserver.py > log/jagare-rpc.log 2>&1 &
}

run_git_server () {
  ./maria/venv/bin/run-maria -p $GIT_SERVER_HTTP_PORT -m http --repos_path $REPOS_PATH > log/maria-http.log 2>&1 &
  ./maria/venv/bin/run-maria -p $GIT_SERVER_SSH_PORT --host-key=./maria/examples/host.key -m ssh --repos_path $REPOS_PATH > log/maria-ssh.log 2>&1 &
}

run () {
  cd $here

  if ! [[ -d $REPOS_PATH ]]; then
    mkdir $REPOS_PATH
  fi

  if ! [[ -d log ]]; then
    mkdir log
  fi

  echo "run git server ..."
  run_git_server

  echo "run git rpc server ..."
  run_git_rpc_server
}

kill_by_port () {
  port=$1
  echo "stop by $port"
  kill -9 `lsof -i:$port -t`
}

case $option in
  "init")
    echo "into init)"
    init
    ;;
  "default"|"run")
    echo "into run)"
    run
    ;;
  "stop")
    kill_by_port $GIT_SERVER_HTTP_PORT
    kill_by_port $GIT_SERVER_SSH_PORT

    kill_by_port $GIT_RPC_SERVER_PORT
    ;;
  *)
    echo "don't know the option."
esac
