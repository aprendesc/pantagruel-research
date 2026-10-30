#!/usr/bin/env python3
"""Stop private content before an upstream push. Do not contact a server."""
import subprocess, sys, re
from urllib.parse import urlsplit

def git(*args):
    return subprocess.check_output(['git', *args], stderr=subprocess.PIPE).decode().strip()

def normalize(url):
    if '://' in url:
        parsed = urlsplit(url)
        host, path = parsed.hostname or '', parsed.path
    else:
        value = url.split('@')[-1]
        host, _, path = value.partition(':')
    host = re.sub(r'^github\.com-.*$', 'github.com', host.lower())
    return host + '/' + path.strip('/').removesuffix('.git').lower()

def private(path):
    parts = path.split('/')
    return (parts[0] in {'context', 'skills', '.agents', '.codex', '.claude', '.githooks', '.worktreelink'}
            or parts[-1] in {'AGENTS.md', 'CLAUDE.md', 'SKILL.md'}
            or path in {'scripts/promote-to-upstream', 'scripts/prepare-upstream-branch'})

def stop(message):
    sys.exit('Push blocked: ' + message)

try:
    downstream = normalize(git('remote', 'get-url', '--push', 'downstream'))
    urls = [normalize(git('remote', 'get-url', 'upstream'))]
    urls += [normalize(x) for x in git('remote', 'get-url', '--push', '--all', 'upstream').splitlines()]
    destination = normalize(sys.argv[2])
    applies = downstream != urls[0] and (sys.argv[1] == 'upstream' or destination in urls)
    refs = sys.stdin.read().splitlines()
    if applies:
        for line in refs:
            local_ref, local_oid, remote_ref, remote_oid = line.split()
            if set(local_oid) == {'0'}:
                continue
            if remote_ref in {'refs/heads/main', 'refs/heads/master', 'refs/heads/develop'}:
                stop('use a reviewed upstream PR; do not push to its base branch.')
            paths = git('ls-tree', '-r', '--name-only', local_oid).splitlines()
            if any(private(x) for x in paths):
                stop('the proposed tree contains private instructions, skills, or context.')
            revision = local_oid if set(remote_oid) == {'0'} else remote_oid + '..' + local_oid
            commits = git('rev-list', revision).splitlines()
            for commit in commits:
                paths = git('diff-tree', '--root', '-m', '--no-commit-id', '--name-only', '-r', commit).splitlines()
                if any(private(x) for x in paths):
                    stop('the proposed history contains private paths; prepare a clean publication branch.')
except (subprocess.CalledProcessError, ValueError, IndexError) as error:
    stop('cannot validate the destination or proposed history: ' + str(error))
