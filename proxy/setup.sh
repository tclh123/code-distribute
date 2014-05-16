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

init () {
  setup $here/tproxy
}

run () {
  cd $here

  if ! [[ -d log ]]; then
    mkdir log
  fi

  echo "run tproxy ..."
  ./tproxy/venv/bin/tproxy routing_script.py -b 0.0.0.0:$TPROXY_PORT > log/tproxy.log 2>&1 &
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
    echo "into stop)"
    kill_by_port $TPROXY_PORT
    ;;
  *)
    echo "don't know the option."
esac
