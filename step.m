clear
clc
warning off

x1min=-5;
x1max=5;
x2min=-5;
x2max=5;
R=1500; % steps resolution
x1=x1min:(x1max-x1min)/R:x1max;
x2=x2min:(x2max-x2min)/R:x2max;

for j=1:length(x1)
    
    % For 1-dimensional plotting
    f1(j)=floor(x1(j)^2);
    
    % For 2-dimensional plotting
    for i=1:length(x2)
        fn(i)=floor(x1(j)^2)+floor(x2(i)^2);
    end
    
    fn_tot(j,:)=fn;

end


figure(1)
meshc(x1,x2,fn_tot);colorbar;set(gca,'FontSize',12);shading interp;
xlabel('x_2','FontName','Times','FontSize',20,'FontAngle','italic');
set(get(gca,'xlabel'),'rotation',25,'VerticalAlignment','bottom');
ylabel('x_1','FontName','Times','FontSize',20,'FontAngle','italic');
set(get(gca,'ylabel'),'rotation',-25,'VerticalAlignment','bottom');
zlabel('f(X)','FontName','Times','FontSize',20,'FontAngle','italic');
title('3D View','FontName','Times','FontSize',24,'FontWeight','bold');