#!/bin/bash

# Crée une branche vide (orphan) pour replay les commits
git checkout main || exit 1
git checkout --orphan step-push || exit 1
git reset --hard

# Liste des commits dans l'ordre chronologique (du plus ancien au plus récent)
COMMITS=$(git rev-list --reverse main)

# Pour chaque commit, cherry-pick et push
for COMMIT in $COMMITS; do
  echo "Cherry-picking commit $COMMIT"
  git cherry-pick $COMMIT || exit 1
  git push origin HEAD || exit 1
done

echo "✅ Tous les commits ont été poussés un par un sur 'step-push'"