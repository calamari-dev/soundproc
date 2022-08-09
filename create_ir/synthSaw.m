function y = synthSaw(f,t,Fs)
    A   = @(k) 2/pi./k.*(-1).^(k-1);
    phi = @(k) 0;    
    y = synthFourier(f,t,A,phi,Fs);
end