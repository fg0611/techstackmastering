import { Controller, Get, UseGuards, UseInterceptors } from '@nestjs/common';
import { UsersService } from './users.service';
import { LoggingInterceptor } from 'src/logging/logging.interceptor';
import { AuthGuard } from 'src/auth/auth.guard';
import { User } from './users.decorator';

@Controller('users')
@UseInterceptors(LoggingInterceptor)
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  @UseGuards(AuthGuard)
  findAll(@User() user: any) {
    console.log('User:', user); // Muestra el usuario extraído
    return this.usersService.findAll();
  }
}