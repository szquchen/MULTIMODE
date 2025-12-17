      subroutine USERIN
      use h2co_pes
      implicit none

      call pes_init()

      return
      end
C****************************************************************
C****************************************************************
      subroutine GETPOT(v,natom,xx,rr)
      use h2co_pes
      implicit none

      double precision v, xx, rr
      integer natom
      dimension xx(natom,3), rr(natom,natom)

      V = h2co_pot(transpose(xx))

      return
      end
C****************************************************************
C****************************************************************
      SUBROUTINE GETQPT
      RETURN
      END
C****************************************************************
C****************************************************************
      SUBROUTINE GETAPT
      RETURN
      END
C****************************************************************
C****************************************************************
      SUBROUTINE GETDIP(v,natom,xx,rr,ldip)
      RETURN
      END
C*****************************
C*****************************
      SUBROUTINE GETQDT
      RETURN
      END
C****************************************************************
C****************************************************************
      SUBROUTINE MINPOT(TAU,NATOM,XR,RR,TAUE)
      RETURN
      END
C****************************************************************
C****************************************************************
      SUBROUTINE DERIV(M,N,X,F)
      RETURN
      END

      SUBROUTINE GETPRP
      RETURN
      END

      SUBROUTINE GETPOL
      RETURN
      END
