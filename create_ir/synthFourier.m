function y = synthFourier(f,t,A,phi,Fs)
    arguments
        f
        t (:,1)
        A
        phi
        Fs
    end

    M = floor(Fs/2/f-eps);
    k = 1:M;
    kft2pi = k.*(f*t*2*pi);
    y = sum(A(k).*sin(kft2pi+phi(k)),2);
end