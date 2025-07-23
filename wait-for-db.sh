#!/bin/sh

# wait-for-db.sh

set -e

host="$1"
shift
cmd="$@"

echo "Waiting for database at $host..."

until mysqladmin ping -h "$host" --silent; do
  echo "Database is unavailable - sleeping"
  sleep 2
done

echo "Database is up - executing command"
exec $cmd
