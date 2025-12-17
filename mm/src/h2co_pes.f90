module h2co_pes
  implicit none

  integer,parameter::ncoff=1561
  integer,parameter ::wp=selected_real_kind(12,300)
  real(kind=wp)::coef(ncoff),pw(ncoff,6)

contains

 subroutine pes_init()
   integer::i
   open(112,status='old',file='./h2co_param/coeff8')
   open(113,status='old',file='./h2co_param/index8')

   read(112,*)
   do i=1,ncoff
     read(112,*) coef(i)
   end do
   do i=1,ncoff
     read(113,*) pw(i,1:6)
   end do
   close(113)
   close(112)

   return
 end subroutine pes_init

 function h2co_pot(cood)
   implicit none
   real(kind=wp)::h2co_pot
   real(kind=wp)::cood(3,4)  
   real(kind=wp)::y(6),r(6)
   real(kind=wp)::bas(ncoff)
    
   call edis(r(1),y(1),cood(:,3),cood(:,4))
   call edis(r(2),y(2),cood(:,2),cood(:,3))
   call edis(r(3),y(3),cood(:,1),cood(:,3))
   call edis(r(4),y(4),cood(:,1),cood(:,4))
   call edis(r(5),y(5),cood(:,2),cood(:,4))
   call edis(r(6),y(6),cood(:,1),cood(:,2))
   call basis(bas,y)

   h2co_pot = dot_product(coef,bas)
   h2co_pot = h2co_pot + 114.332958863 - 0.0001028161

   return
 end function h2co_pot

 subroutine edis(dis,edist,atomi,atomj)
   real(kind=wp)::atomi(3),atomj(3)
   real(kind=wp)::dis,alfa,dr(3)
   real(kind=wp),intent(out)::edist
   alfa=2.0
   dr=atomi-atomj
   dis=norm2(dr)
   edist=exp(-dis/alfa)
   return
 end subroutine edis

 subroutine basis(bas,y)
   integer m,n,p,q,i,j,k
   real(kind=wp)::bas(ncoff)
   real(kind=wp)::y(6)
   do k=1,ncoff
      bas(k)=(y(1)**pw(k,1)) * (y(6)**pw(k,6)) * &
           & ((y(2)**pw(k,2))*(y(3)**pw(k,3))*(y(4)**pw(k,4))*(y(5)**pw(k,5))+ &
           &  (y(2)**pw(k,5))*(y(3)**pw(k,4))*(y(4)**pw(k,3))*(y(5)**pw(k,2)))
   end do

   return
 end subroutine

end module h2co_pes
