# LCDM Twin Launch Plan

Date: 2026-08-06

Purpose: launch `cmp_lcdm_ev.yaml` on the same AWS build after the dyad leg finishes, with the
same runtime stack and the same solo-PolyChord rule.

## Preconditions

1. `cmp_prtoe_dyad_ev` is no longer running.
2. No other `cobaya.run` or `polychord` process is alive on the instance.
3. The AWS box still uses:
   - repo root: `/home/ubuntu/prtoe_class`
   - venv: `/home/ubuntu/venv`
   - packages path: `/home/ubuntu/cobaya_packages_clean`
   - candl data: `/home/ubuntu/candl_data`
4. `cmp_lcdm_ev.yaml` exists on the instance at `/home/ubuntu/prtoe_class/cmp_lcdm_ev.yaml`.
   If not, copy the current repo version there before launch.

Current observed AWS state on 2026-08-06: `cmp_lcdm_ev.yaml` is missing on the instance, so that
copy step is currently mandatory.

## Fresh-Launch Rule

Mirror the repo's own evidence-pair rule:

- move any stale `chains/cmp_lcdm_ev_polychord_raw` aside
- move any stale `cmp_lcdm_ev.aws.launchlog` aside
- launch fresh with `-f`
- keep the run solo: no concurrent Cobaya job

## Preflight Commands

```bash
pgrep -af '[m]pirun|[c]obaya.run|[p]olychord'
test -f /home/ubuntu/prtoe_class/cmp_lcdm_ev.yaml
ls -lah /home/ubuntu/prtoe_class/chains/cmp_lcdm_ev_polychord_raw 2>/dev/null || true
```

## Launch Command

Run on the EC2 instance as `root`:

```bash
STAMP=$(date +%Y%m%d_%H%M%S)
[ -d /home/ubuntu/prtoe_class/chains/cmp_lcdm_ev_polychord_raw ] && \
  mv /home/ubuntu/prtoe_class/chains/cmp_lcdm_ev_polychord_raw \
     /home/ubuntu/prtoe_class/chains/cmp_lcdm_ev_polychord_raw.stale.$STAMP
[ -f /home/ubuntu/prtoe_class/cmp_lcdm_ev.aws.launchlog ] && \
  mv /home/ubuntu/prtoe_class/cmp_lcdm_ev.aws.launchlog \
     /home/ubuntu/prtoe_class/cmp_lcdm_ev.aws.launchlog.stale.$STAMP
sudo -u ubuntu -H bash -lc '
  source /home/ubuntu/venv/bin/activate &&
  export OMP_NUM_THREADS=1 &&
  cd /home/ubuntu/prtoe_class &&
  nohup mpirun -n 16 --bind-to none python -m cobaya.run cmp_lcdm_ev.yaml -f \
    > cmp_lcdm_ev.aws.launchlog 2>&1 &
  echo $! > /home/ubuntu/prtoe_class/cmp_lcdm_ev.aws.pid
'
```

## Immediate Postflight Checks

```bash
cat /home/ubuntu/prtoe_class/cmp_lcdm_ev.aws.pid
pgrep -af '[m]pirun.*cmp_lcdm_ev|[c]obaya.run.*cmp_lcdm_ev|[p]olychord'
tail -n 80 /home/ubuntu/prtoe_class/cmp_lcdm_ev.aws.launchlog
ls -lah /home/ubuntu/prtoe_class/chains/cmp_lcdm_ev_polychord_raw
```

## Success Markers

- `prterun` is live
- `python -m cobaya.run cmp_lcdm_ev.yaml -f` ranks are live
- log reaches `Calling PolyChord...`
- raw dir exists and starts writing:
  - `cmp_lcdm_ev.resume`
  - `cmp_lcdm_ev_phys_live.txt`

## Failure Markers

- no live `mpirun` / `cobaya.run` process after launch
- log ends before `Calling PolyChord...`
- no raw dir created
- output appears under `/home/ubuntu/chains/...` instead of `/home/ubuntu/prtoe_class/chains/...`

## Pair-Completion Rule

The nested verdict is still not bookable until both:

1. `cmp_prtoe_dyad_ev`
2. `cmp_lcdm_ev`

finish on the same AWS build and produce their final PolyChord stats files.
