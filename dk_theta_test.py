"""
Test the sec.59 conjecture: is delta-K (kinetic fluctuation that funds the DE
floor, (deltaK)^2 operator) the SAME field as Theta (multi-stream/granule
density fluctuation that flips m_e)? Both are consequences of multi-streaming
in the wave-DM condensate. Build the interference field, compute both, correlate.
"""
import numpy as np
np.random.seed(7)

def wave_field(N_streams, grid=96, kspread=0.0, k0=6.0):
    """Superpose N plane waves (a monochromatic-ish shell |k|~k0) with random
    directions + phases -> the granule/speckle field psi on a periodic box."""
    L=2*np.pi; x=np.linspace(0,L,grid,endpoint=False)
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    psi=np.zeros((grid,)*3,dtype=complex)
    for _ in range(N_streams):
        # random direction on the sphere, magnitude k0 (+ optional spread)
        d=np.random.randn(3); d/=np.linalg.norm(d)
        kmag=k0*(1+kspread*np.random.randn())
        kx,ky,kz=(np.round(d*kmag)).astype(int)  # integer modes (periodic)
        ph=np.random.uniform(0,2*np.pi)
        psi+=np.exp(1j*(kx*X+ky*Y+kz*Z+ph))
    return psi,(X,Y,Z)

def fields(psi):
    """rho=|psi|^2 (Theta/granule density) ; T=|grad psi|^2/2 (kinetic -> deltaK)."""
    rho=np.abs(psi)**2
    # spectral gradient
    g=psi.shape[0]; k=np.fft.fftfreq(g,d=1.0/g)*1.0
    KX,KY,KZ=np.meshgrid(k,k,k,indexing='ij')
    ph=np.fft.fftn(psi)
    gx=np.fft.ifftn(1j*KX*ph); gy=np.fft.ifftn(1j*KY*ph); gz=np.fft.ifftn(1j*KZ*ph)
    T=0.5*(np.abs(gx)**2+np.abs(gy)**2+np.abs(gz)**2)   # kinetic energy density
    return rho,T

def corr(a,b):
    da=a-a.mean(); db=b-b.mean()
    return float((da*db).mean()/np.sqrt((da*da).mean()*(db*db).mean()))

print(f"{'N_streams':>9} {'S=Var(rho)/<rho>^2':>18} {'Var(T)/<T>^2':>13} {'r(dRho,dK)':>11}")
print("-"*56)
for N in [1,2,3,5,10,30,100]:
    psi,_=wave_field(N)
    rho,T=fields(psi)
    S=rho.var()/rho.mean()**2
    VT=T.var()/T.mean()**2
    r=corr(rho,T)
    tag=" <- single stream: both flat" if N==1 else ""
    print(f"{N:>9} {S:>18.4f} {VT:>13.4f} {r:>11.4f}{tag}")

# high-statistics correlation at a representative multi-stream N, averaged over realizations
print("\nCorrelation r(delta-rho, delta-K) averaged over 12 realizations:")
for N in [5,30,100]:
    rs=[]
    for s in range(12):
        np.random.seed(100+s)
        psi,_=wave_field(N)
        rho,T=fields(psi)
        rs.append(corr(rho,T))
    print(f"  N={N:>3}:  r = {np.mean(rs):.3f} +/- {np.std(rs):.3f}")
